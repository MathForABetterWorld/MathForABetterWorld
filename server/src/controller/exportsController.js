import validate from "../util/checkValidation.js";
import prisma from "../../prisma/client.js";
import { StatusCodes } from "http-status-codes";

export const createExport = async (req, res) => {
  if (validate(req, res)) {
    return res;
  }
  const { weight, categoryId, donatedTo, userId } = req.body;
  const exportItem = await prisma.exportItem.create({
    data: {
      weight,
      userId,
      donatedTo,
      categoryId,
    },
  });
  return res.status(StatusCodes.CREATED).json({ exportItem });
};

export const getExports = async (req, res) => {
  if (validate(req, res)) {
    return res;
  }
  const exports = await prisma.exportItem.findMany();
  return res.status(StatusCodes.ACCEPTED).json({ exports });
};

export const deleteExport = async (req, res) => {
  if (validate(req, res)) {
    return res;
  }
  const id = parseInt(req.params.id, 10);
  const deletedExport = await prisma.exportItem.delete({ where: { id } });
  return res.status(StatusCodes.ACCEPTED).json({ deleteExport });
};

export const editExport = async (req, res) => {
  if (validate(req, res)) {
    return res;
  }
  const { weight, categoryId, donatedTo, userId, id } = req.body;
  const exportItem = await prisma.exportItem.update({
    where: {
      id,
    },
    data: {
      weight,
      userId,
      donatedTo,
      categoryId,
    },
  });
  return res.status(StatusCodes.CREATED).json({ exportItem });
};
