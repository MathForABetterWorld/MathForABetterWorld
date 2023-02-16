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
  return res.status(StatusCodes.CREATED).json(distributor);
};
