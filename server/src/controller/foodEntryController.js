import validate from "../util/checkValidation.js";
import prisma from "../../prisma/client.js";
import { StatusCodes } from "http-status-codes";

/**
 * Creates a food entry
 * @param {object} req - request for the course
 * @param {object} res - response for the request
 */
export const createFoodEntry = async (req, res) => {
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
  const foodEntry = await prisma.foodEntry.create({
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
  return res.status(StatusCodes.CREATED).json({ foodEntry });
};

/**
 * Gets list of food entrys
 * @param {object} req - request for the course
 * @param {object} res - response for the request
 */
export const getFoodEntrys = async (req, res) => {
  const foodEntry = await prisma.foodEntry.findMany();
  return res.status(StatusCodes.ACCEPTED).json({ foodEntry });
};

/**
 * Deletes a food entry
 * @param {object} req - request for the course
 * @param {object} res - response for the request
 */
export const deleteFoodEntry = async (req, res) => {
  const id = parseInt(req.params.id, 10);
  const foodEntry = await prisma.foodEntry.delete({
    where: {
      id,
    },
  });
  return res.status(StatusCodes.ACCEPTED).json({ foodEntry });
};

/**
 * Edits a food entry
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
    categoryId,
  } = req.body;
  const id = parseInt(req.params.id, 10);
  const foodEntry = await prisma.foodEntry.update({
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
      categoryId,
    },
  });
  return res.status(StatusCodes.ACCEPTED).json({ foodEntry });
};