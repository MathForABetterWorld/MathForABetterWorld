import validate from "../util/checkValidation.js";
import prisma from "../../prisma/client.js";
import { StatusCodes } from "http-status-codes";

/**
 * Creates a pallot
 * @param {object} req - request for the course
 * @param {object} res - response for the request
 */
export const createPallot = async (req, res) => {
  if (validate(req, res)) {
    return res;
  }
  const {
    entryUserId,
    inputDate,
    expirationDate,
    weight,
    companyId,
    rackId,
    inWarehouse,
    description,
    categoryId,
  } = req.body;
  const Pallot = await prisma.Pallot.create({
    data: {
      entryUserId,
      inputDate: new Date(inputDate),
      expirationDate: new Date(expirationDate),
      weight,
      companyId,
      rackId,
      inWarehouse,
      description,
      categoryId,
    },
  });
  return res.status(StatusCodes.CREATED).json({ Pallot });
};

/**
 * Gets list of pallots
 * @param {object} req - request for the course
 * @param {object} res - response for the request
 */
export const getPallots = async (req, res) => {
  const Pallot = await prisma.Pallot.findMany();
  return res.status(StatusCodes.ACCEPTED).json({ Pallot });
};

/**
 * Gets the soonest expiring pallot
 * @param {object} req - request for the course
 * @param {object} res - response for the request
 */
export const getSoonestExpiringPallot = async (req, res) => {
  const Pallots = await prisma.pallot.findMany({
    // only care about pallots that are in the warehouse
    where: {
      inWarehouse: true,
    },
    orderBy: {
      expirationDate: "asc", // I assume this sorts in ascending order
    },
  });
  if (Pallots.length === 0) {
    return res.status(StatusCodes.NOT_FOUND).json({
      message: "No pallots in warehouse found",
    });
  }
  let soonestExpiringPallot = Pallots[0];
  // for (const Pallot of Pallots) {
  //   if (Pallot.expirationDate < soonestExpiringPallot.expirationDate) {
  //     soonestExpiringPallot = Pallot
  //   }
  // }
  return res.status(StatusCodes.ACCEPTED).json({ soonestExpiringPallot });
};

/**
 * Deletes a pallot
 * @param {object} req - request for the course
 * @param {object} res - response for the request
 */
export const deletePallot = async (req, res) => {
  const id = parseInt(req.params.id, 10);
  const Pallot = await prisma.Pallot.delete({
    where: {
      id,
    },
  });
  return res.status(StatusCodes.ACCEPTED).json({ Pallot });
};

/**
 * Edits a pallot
 * @param {object} req - request for the course
 * @param {object} res - response for the request
 */
export const edit = async (req, res) => {
  if (validate(req, res)) {
    return res;
  }
  const {
    entryUserId,
    inputDate,
    expirationDate,
    weight,
    companyId,
    rackId,
    inWarehouse,
    description,
    categoryIds,
  } = req.body;
  const id = parseInt(req.params.id, 10);
  const Pallot = await prisma.Pallot.update({
    where: {
      id,
    },
    data: {
      entryUserId,
      inputDate,
      expirationDate,
      weight,
      companyId,
      rackId,
      inWarehouse,
      description,
      categoryIds,
    },
  });
  return res.status(StatusCodes.ACCEPTED).json({ Pallot });
};

/**
 * gets all pallots containing a specific category
 * @param {object} req - request for the course
 * @param {object} res - response for the request
 */
export const getPallotsForCategory = async (req, res) => {
  if (validate(req, res)) {
    return res;
  }
  const categoryId = parseInt(req.params.categoryId, 10);
  const Pallot = await prisma.Pallot.findMany({
    where: {
      categoryIds: {
        has: categoryId,
      },
    },
  });
  return res.status(StatusCodes.ACCEPTED).json({ Pallot });
};

/**
 * gets every category in a pallot
 * @param {object} req - request for the course
 * @param {object} res - response for the request
 */
export const getCategoriesForPallot = async (req, res) => {
  if (validate(req, res)) {
    return res;
  }
  const id = parseInt(req.params.id, 10);
  const Pallot = await prisma.Pallot.findUnique({
    where: {
      id,
    },
  });
  const categories = await prisma.category.findMany({
    where: {
      id: {
        in: Pallot.categoryIds,
      },
    },
  });
  return res.status(StatusCodes.ACCEPTED).json({ categories });
};

/**
 * returns data with weight per day
 * @param {object} req - request for the course
 * @param {object} res - response for the request
 */
export const returnWeightPerDay = async (req, res) => {
  if (validate(req, res)) {
    return res;
  }
  const groupWeight = await prisma.Pallot.groupBy({
    by: ["inputDate"],
    _sum: {
      weight,
    },
  });
  return res.status(StatusCodes.ACCEPTED).json({ groupWeight });
};

/**
 * Gets total count of pallots
 * @param {object} req - request for the course
 * @param {object} res - response for the request
 */
export const getPallotsCount = async (req, res) => {
  if (validate(req, res)) {
    return res;
  }
  const pallotsCount = await prisma.Pallot.count();
  return res.status(StatusCodes.OK).json({ pallotsCount });
};

export const removePallot = async (req, res) => {
  if (validate(req, res)) {
    return res;
  }
  const { id } = req.body;
  const pallot = await prisma.Pallot.update({
    where: {
      id,
    },
    data: {
      inWarehouse: false,
      rackId: null,
    },
  });
  return res.status(StatusCodes.ACCEPTED).json({ pallot });
};
