import prisma from "../../prisma/client.js";
import { StatusCodes } from "http-status-codes";

export const isUserId = async (req, res, next) => {
  const { userId } = req.body;
  const user = await prisma.user.findUnique({ where: { id: userId } });
  if (user === null || user === undefined) {
    return res
      .status(StatusCodes.BAD_REQUEST)
      .json({ msg: "ERROR: user does not exist" });
  } else {
    next();
  }
};

export const isCategoryId = async (req, res, next) => {
  const { categoryId } = req.body;
  const category = await prisma.category.findUnique({
    where: { id: categoryId },
  });
  if (category === null || category === undefined) {
    return res
      .status(StatusCodes.BAD_REQUEST)
      .json({ msg: "ERROR: this is not a valid category id" });
  } else {
    next();
  }
};

export const isExportIdParam = async (req, res, next) => {
  const id = parseInt(req.params.id, 10);
  const exportItem = await prisma.exportItem.findUnique({ where: { id } });
  if (exportItem === null || exportItem === undefined) {
    return res
      .status(StatusCodes.BAD_REQUEST)
      .json({ msg: "ERROR: there is no export with this id" });
  } else {
    next();
  }
};

export const isExportId = async (req, res, next) => {
  const { id } = req.body;
  const exportItem = await prisma.exportItem.findUnique({ where: { id } });
  if (exportItem === null || exportItem === undefined) {
    return res
      .status(StatusCodes.BAD_REQUEST)
      .json({ msg: "ERROR: there is no export with this id" });
  } else {
    next();
  }
};

export const isLocationIdOptional = async (req, res, next) => {
  const { locationId } = req.body;
  if (locationId !== null && locationId !== undefined) {
    const location = await prisma.location.findUnique({
      where: { id: locationId },
    });
    if (location === null || location === undefined) {
      return res
        .status(StatusCodes.BAD_REQUEST)
        .json({ msg: "ERROR: location id is invalid" });
    } else {
      next();
    }
  } else {
    next();
  }
};
