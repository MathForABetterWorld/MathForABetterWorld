import prisma from "../../prisma/client.js";
import { StatusCodes } from "http-status-codes";

export const isUniqueName = async (req, res, next) => {
  const { name } = req.body;
  const query = await prisma.distributor.findFirst({
    where: {
      name,
    },
  });
  if (query !== null) {
    return res
      .status(StatusCodes.CONFLICT)
      .json({ msg: "ERROR: distributor with this name already exists" });
  } else {
    next();
  }
};

export const isDistributorIdParams = async (req, res, next) => {
  const id = parseInt(req.params.id, 10);
  const query = await prisma.distributor.findUnique({
    where: {
      id,
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

export const isDistributorIdBody = async (req, res, next) => {
  const {id} = req.body;
  const query = await prisma.distributor.findUnique({
    where: {
      id,
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
