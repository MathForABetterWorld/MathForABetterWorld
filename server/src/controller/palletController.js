import validate from "../util/checkValidation.js";
import prisma from "../../prisma/client.js";
import { StatusCodes } from "http-status-codes";

/**
 * Creates a pallet
 * @param {object} req - request for the course
 * @param {object} res - response for the request
 */
export const createPallet = async (req, res) => {
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
    description,
    categoryId,
  } = req.body;
  console.log("createpallet called: ", req.body)
  const Pallet = await prisma.Pallet.create({
    data: {
      entryUserId,
      inputDate: new Date(inputDate),
      expirationDate: new Date(expirationDate),
      weight,
      companyId,
      rackId,
      description,
      categoryId,
    },
  });
  return res.status(StatusCodes.CREATED).json({ Pallet });
};

/**
 * Gets list of pallets
 * @param {object} req - request for the course
 * @param {object} res - response for the request
 */
export const getPallets = async (req, res) => {
  const Pallet = await prisma.Pallet.findMany({
    include: {
      company: true,
    },
  });
  return res.status(StatusCodes.ACCEPTED).json({ Pallet });
};

/**
 * Gets the soonest expiring pallet
 * @param {object} req - request for the course
 * @param {object} res - response for the request
 */
export const getSoonestExpiringPallet = async (req, res) => {
  const Pallets = await prisma.pallet.findMany({
    // only care about pallets that are in the warehouse
    orderBy: {
      expirationDate: "asc", // I assume this sorts in ascending order
    },
  });
  if (Pallets.length === 0) {
    return res.status(StatusCodes.NOT_FOUND).json({
      message: "No pallets in warehouse found",
    });
  }
  let soonestExpiringPallet = Pallets[0];
  // for (const Pallet of Pallets) {
  //   if (Pallet.expirationDate < soonestExpiringPallet.expirationDate) {
  //     soonestExpiringPallet = Pallet
  //   }
  // }
  return res.status(StatusCodes.ACCEPTED).json({ soonestExpiringPallet });
};

/**
 * Deletes a pallet
 * @param {object} req - request for the course
 * @param {object} res - response for the request
 */
export const deletePallet = async (req, res) => {
  const id = parseInt(req.params.id, 10);
  const Pallet = await prisma.Pallet.delete({
    where: {
      id,
    },
  });
  return res.status(StatusCodes.ACCEPTED).json({ Pallet });
};

/**
 * Edits a pallet
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
    description,
    categoryIds,
  } = req.body;
  const id = parseInt(req.params.id, 10);
  const Pallet = await prisma.Pallet.update({
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
      description,
      categoryIds,
    },
  });
  return res.status(StatusCodes.ACCEPTED).json({ Pallet });
};

/**
 * gets all pallets containing a specific category
 * @param {object} req - request for the course
 * @param {object} res - response for the request
 */
export const getPalletsForCategory = async (req, res) => {
  if (validate(req, res)) {
    return res;
  }
  const categoryId = parseInt(req.params.categoryId, 10);
  const Pallet = await prisma.Pallet.findMany({
    where: {
      categoryIds: {
        has: categoryId,
      },
    },
  });
  return res.status(StatusCodes.ACCEPTED).json({ Pallet });
};

/**
 * gets every category in a pallet
 * @param {object} req - request for the course
 * @param {object} res - response for the request
 */
export const getCategoriesForPallet = async (req, res) => {
  if (validate(req, res)) {
    return res;
  }
  const id = parseInt(req.params.id, 10);
  const Pallet = await prisma.Pallet.findUnique({
    where: {
      id,
    },
  });
  const categories = await prisma.category.findMany({
    where: {
      id: {
        in: Pallet.categoryIds,
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
  const groupWeight = await prisma.Pallet.groupBy({
    by: ["inputDate"],
    _sum: {
      weight,
    },
  });
  return res.status(StatusCodes.ACCEPTED).json({ groupWeight });
};

/**
 * Gets total count of pallets
 * @param {object} req - request for the course
 * @param {object} res - response for the request
 */
export const getPalletsCount = async (req, res) => {
  if (validate(req, res)) {
    return res;
  }
  const palletsCount = await prisma.Pallet.count();
  return res.status(StatusCodes.OK).json({ palletsCount });
};

export const removePallet = async (req, res) => {
  if (validate(req, res)) {
    return res;
  }
  const { id } = req.body;
  const pallet = await prisma.Pallet.update({
    where: {
      id,
    },
    data: {
      rackId: null,
    },
  });
  return res.status(StatusCodes.ACCEPTED).json({ pallet });
};
