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
