import validate from "../util/checkValidation.js";
import prisma from "../../prisma/client.js";
import { StatusCodes } from "http-status-codes";

export const createExport = async (req, res) => {
  if (validate(req, res)) {
    return res;
  }
  const { weight, categoryId, donatedTo, userId, locationId, exportType } =
    req.body;
  if (donatedTo == "BCF Curbside" && exportType == "Return") {
    weight *= -1;
  }
  const exportItem = await prisma.exportItem.create({
    data: {
      weight,
      userId,
      donatedTo,
      categoryId,
      locationId,
      exportType,
    },
  });
  return res.status(StatusCodes.CREATED).json({ exportItem });
};

export const getExports = async (req, res) => {
  if (validate(req, res)) {
    return res;
  }
  const exports = await prisma.exportItem.findMany({
    include: {
      category: true,
      location: true,
      user: {
        select: {
          name: true,
        },
      },
    },
  });
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
  const { weight, categoryId, donatedTo, userId, id, locationId, exportType } =
    req.body;
  const exportItem = await prisma.exportItem.update({
    where: {
      id,
    },
    data: {
      weight,
      userId,
      donatedTo,
      categoryId,
      locationId,
      exportType,
    },
  });
  return res.status(StatusCodes.CREATED).json({ exportItem });
};

export const getExportsInDuration = async (req, res) => {
  const { duration } = req.params;
  const startDate = new Date();
  if (duration === "day") {
    startDate.setDate(startDate.getDate() - 1);
  } else if (duration === "week") {
    startDate.setDate(startDate.getDate() - 7);
  } else if (duration === "month") {
    startDate.setMonth(startDate.getMonth() - 1);
  } else {
    startDate.setFullYear(startDate.getFullYear() - 1);
  }
  startDate.setUTCHours(0);
  startDate.setUTCMinutes(0);
  startDate.setUTCSeconds(0);
  startDate.setUTCMilliseconds(0);
  const exportTotalInDuration = await prisma.exportItem.aggregate({
    _sum: {
      weight: true,
    },
    where: {
      exportDate: {
        gte: startDate,
      },
    },
  });
  return res.status(StatusCodes.ACCEPTED).json({ exportTotalInDuration });
};
