import prisma from "../../prisma/client.js";
import { StatusCodes } from "http-status-codes";

export const isRackId = async (req, res, next) => {
  const id = parseInt(req.params.id, 10);
  const query = await prisma.rack.findUnique({
    where: {
      id,
    },
  });
  if (query === null || query === undefined) {
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
  if (query !== null) {
    return res
      .status(StatusCodes.CONFLICT)
      .json({ msg: "ERROR: rack with this location already exists" });
  } else {
    next();
  }
};

export const isUniqueLocationNotId = async (req, res, next) => {
  const { location } = req.body;
  const id = parseInt(req.params.id, 10);
  const query = await prisma.rack.findFirst({
    where: {
      location,
    },
  });
  if (query !== null && query.id !== id) {
    return res
      .status(StatusCodes.CONFLICT)
      .json({ msg: "ERROR: rack with this location already exists" });
  } else {
    next();
  }
};

export const weightIsPositive = async (req, res, next) => {
  const { weightLimit } = req.body;
  if (weightLimit === null || weightLimit === undefined) {
    next();
  } else if (weightLimit <= 0) {
    return res
      .status(StatusCodes.BAD_REQUEST)
      .json({ msg: "Weight Limit must be positive" });
  } else {
    next();
  }
};
