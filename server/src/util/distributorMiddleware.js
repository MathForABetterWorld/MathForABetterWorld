import prisma from "../../prisma/client.js";
import { StatusCodes } from "http-status-codes";

export const isUniqueName = async (req, res, next) => {
  const { name } = req.body;
  const query = await prisma.distributor.findFirst({
    where: {
      name,
    },
  });
  if (query !== NULL) {
    return res
      .status(StatusCodes.CONFLICT)
      .json({ msg: "ERROR: distributor with this name already exists" });
  } else {
    next();
  }
};

export const isDistributorId = async (req, res, next) => {
  const id = parseInt(req.params.id, 10);
  const query = await prisma.distributor.findUnique({
    where: {
      id,
    },
  });
  if (query === NULL || query === undefined) {
    return res
      .status(StatusCodes.CONFLICT)
      .json({ msg: "ERROR: distributor does not exist" });
  } else {
    next();
  }
};
