import { isPrismaError, prismaErrorToHttpError } from "./helpers.js";

// export const checkToken = (req, res, next) => {
//   const bearerHeader = req.headers["authorization"];
//   if (bearerHeader) {
//     const bearer = bearerHeader.split(" ");
//     const token = bearer[1];
//     // check the token or attach it to the request object!
//     req.token = token;
//   }
//   next();
// };

export const checkToken = async (req, res, next) => {
  debug(`checkToken is called!`);
  try {
    const bearerHeader = req.headers["authorization"];
    debug(`Read the authorization header...`);
    if (!bearerHeader) {
      throw new ApiError(401, "No authorization token was provided!");
    }
    debug(`Extract the token from auth header...`);
    const bearer = bearerHeader.split(" ");
    const token = bearer[1];

    debug(`Decoding the token ...`);
    const { iat, exp, ...userInfo } = decodeToken(token);
    const account = await prisma.employee.findUnique({
      where: {
        id: userInfo.id,
      },
      include: {
        user: true,
      },
    });
    if (account == null || account == undefined) {
      throw new ApiError(404, "Authorization token not found!");
    } else if (
      account.userName != userInfo.userName ||
      account.user.name != userInfo.user.name ||
      account.user.email != userInfo.user.email
    ) {
      throw new ApiError(401, "Invalid Authorization token was provided!");
    }
    debug(`Token belongs to ${userInfo.username}`);

    debug(
      `Attaching user and token (and its decoded expirtation date) to the req object`
    );
    req.user = userInfo;
    req.id = userInfo.id;
    req.token = {
      value: token,
      expiresIn: exp,
      issuedAt: iat,
    };
    debug(`checkToken is done!`);
    next();
  } catch (err) {
    debug(`Error in checkToken: ${JSON.stringify(err, null, 2)}`);
    if (err && err.name === "TokenExpiredError") {
      next(new ApiError(401, "Authorization token expired!"));
    } else if (err && err.name === "JsonWebTokenError") {
      next(new ApiError(401, `Authorization error ${err.message}`));
    } else {
      next(err);
    }
  }
};

export const globalErrorHandler = (err, req, res, next) => {
  if (err) {
    // console.log(err);
    if (
      (err.name && err.name === "NotFoundError") ||
      (err.name && err.name === "RecordNotFound")
    ) {
      // Prisma throws NotFoundError when findUnique fails to find the resource!
      // It throws RecordNotFound when delete or update operations fail to find the record.
      return res.status(404).json({ message: err.message });
    } else if (isPrismaError(err)) {
      // Check for other Prisma Errors
      prismaErrorToHttpError(err, res);
    } else {
      return res
        .status(err.status || 500)
        .json({ message: err.message || "Internal server error!" });
    }
  }
  next();
};
