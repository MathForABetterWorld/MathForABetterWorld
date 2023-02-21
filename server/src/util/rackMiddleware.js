import prisma from "../../prisma/client.js";
import { StatusCodes } from "http-status-codes";


export const isRackId = async (req, res, next) => {
    const id = parseInt(req.params.id, 10);
    const query = await prisma.rack.findUnique({
      where: {
        id,
      },
    });
    if (query === NULL || query === undefined) {
      return res
        .status(StatusCodes.CONFLICT)
        .json({ msg: "ERROR: rack does not exist" });
    } else {
      next();
    }
};

export const isUniqueLocation = async (req, res, next) => {
  const { location } = req.body;
  const query = await prisma.rack.findFirst({
    where: {
        location,
    },
  });
  if (query !== NULL) {
    return res
      .status(StatusCodes.CONFLICT)
      .json({ msg: "ERROR: rack with this location already exists" });
  } else {
    next();
  }
};
