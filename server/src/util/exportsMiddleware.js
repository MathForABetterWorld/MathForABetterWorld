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

export const isLocationId = async (req, res, next) => {
  const { locationId } = req.body;
  const location = await prisma.donationLocation.findUnique({
    where: { id: locationId },
  });
  if (location === null || location === undefined) {
    return res
      .status(StatusCodes.BAD_REQUEST)
      .json({ msg: "ERROR: this is not a valid location id" });
  } else {
    next();
  }
};

export const returnIsBCF = async (req, res, next) => {
  const { locationId, exportType } = req.body;
  const location = await prisma.donationLocation.findUnique({
    where: { id: locationId },
  });
  if (
    location !== "BCF Curbside - Remington" &&
    location !== "BCF Curbside - Sandtown" &&
    exportType === "Return"
  ) {
    return res
      .status(StatusCodes.BAD_REQUEST)
      .json({ msg: "ERROR: only food from BCF Curbside is returned" });
  } else {
    next();
  }
};

export const weightUsuallyPositive = async (req, res, next) => {
  const { exportType, weight } = req.body;
  if (exportType === "Return" || weight < 0) {
    return res
      .status(StatusCodes.BAD_REQUEST)
      .json({ msg: "ERROR: only food returned has negative weight" });
  } else {
    next();
  }
};
