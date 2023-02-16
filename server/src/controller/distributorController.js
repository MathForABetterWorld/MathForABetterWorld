import validate from "../util/checkValidation.js";
import prisma from "../../prisma/client.js";
import { StatusCodes } from "http-status-codes";

export const createDistributor = async (req, res) => {
  if (validate(req, res)) {
    return res;
  }
  const { name } = req.body;
  const distributor = await prisma.distributor.create({
    data: {
      name,
    },
  });
  return res.status(StatusCodes.CREATED).json({ distributor });
};

export const getDistributors = async (req, res) => {
  const distributors = await prisma.distributor.findMany();
  return res.status(StatusCodes.ACCEPTED).json({ distributors });
};

export const deleteDistributor = async (req, res) => {
  const id = parseInt(req.params.id, 10);
  const distributor = await prisma.distributor.delete({
    where: {
      id,
    },
  });
  return res.status(StatusCodes.ACCEPTED).json({ distributor });
};
