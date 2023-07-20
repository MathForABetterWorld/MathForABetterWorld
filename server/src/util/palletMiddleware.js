import prisma from "../../prisma/client.js";
import { StatusCodes } from "http-status-codes";

/**
 * checks if the pallet being entered exists
 * @param {object} req - request
 * @param {object} res - response
 * @param {object} next - call back function
 */
export const isPalletId = async (req, res, next) => {
  const id = parseInt(req.params.id, 10);
  const query = await prisma.pallet.findUnique({
    where: {
      id,
    },
  });
  if (query === null || query === undefined) {
    return res
      .status(StatusCodes.CONFLICT)
      .json({ msg: "ERROR: pallet id does not exist" });
  } else {
    next();
  }
};
export const isPalletIdBody = async (req, res, next) => {
  const { id } = req.body;
  const query = await prisma.pallet.findUnique({
    where: {
      id,
    },
  });
  if (query === null || query === undefined) {
    return res
      .status(StatusCodes.CONFLICT)
      .json({ msg: "ERROR: pallet id does not exist" });
  } else {
    next();
  }
};

/**
 * checks the expiration date is still good
 * @param {object} req - request
 * @param {object} res - response
 * @param {object} next - call back function
 */
export const isExpired = (req, res, next) => {
  const { expirationDate, inputDate } = req.body;
  const exp = new Date(expirationDate);
  const input = new Date(inputDate);
  input.setDate(input.getDate() + 4);
  if (exp.getTime() < input.getTime()) {
    res.status(StatusCodes.BAD_REQUEST).json({
      msg: "ERROR: expiration date has passed or is less than 4 days away",
    });
  } else {
    next();
  }
};

/**
 * checks if the distributor being entered exists
 * @param {object} req - request
 * @param {object} res - response
 * @param {object} next - call back function
 */
export const isDistributorId = async (req, res, next) => {
  const { companyId } = req.body;
  const query = await prisma.distributor.findUnique({
    where: {
      id: companyId,
    },
  });
  if (query === null || query === undefined) {
    return res
      .status(StatusCodes.CONFLICT)
      .json({ msg: "ERROR: distributor does not exist" });
  } else {
    next();
  }
};

/**
 * checks if the entry user exists
 * @param {object} req - request
 * @param {object} res - response
 * @param {object} next - call back function
 */
export const isUserId = async (req, res, next) => {
  const { entryUserId } = req.body;
  const query = await prisma.user.findUnique({
    where: {
      id: entryUserId,
    },
  });
  if (query === null || query === undefined) {
    return res
      .status(StatusCodes.CONFLICT)
      .json({ msg: "ERROR: user does not exist" });
  } else {
    next();
  }
};

/**
 * checks if the rack exists
 * @param {object} req - request
 * @param {object} res - response
 * @param {object} next - call back function
 */
export const isRack = async (req, res, next) => {
  const { rackId } = req.body;
  if (rackId === null || rackId === undefined) {
    next();
  } else {
    const query = await prisma.rack.findUnique({
      where: {
        id: rackId,
      },
    });
    if (query === null || query === undefined) {
      return res
        .status(StatusCodes.CONFLICT)
        .json({ msg: "ERROR: rack does not exist" });
    } else {
      next();
    }
  }
};

/**
 * checks if the category exists
 * @param {object} req - request
 * @param {object} res - response
 * @param {object} next - call back function
 */
export const isCategory = async (req, res, next) => {
  const { categoryIds } = req.body;
  const query = await prisma.category.findMany({
    where: {
      id: {
        in: categoryIds,
      },
    },
  });
  if (query === null || query === undefined) {
    return res
      .status(StatusCodes.CONFLICT)
      .json({ msg: "ERROR: category does not exist" });
  } else {
    next();
  }
};

/**
 * checks if weight is positive
 * @param {object} req - request
 * @param {object} res - response
 * @param {object} next - call back function
 */
export const isPositiveWeight = (req, res, next) => {
  const { weight } = req.body;
  if (weight <= 0) {
    res.status(StatusCodes.BAD_REQUEST).json({
      msg: "ERROR: weight is less than 0",
    });
  } else {
    next();
  }
};