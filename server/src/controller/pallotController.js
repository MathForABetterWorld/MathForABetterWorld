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
    categoryId,
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
      categoryId,
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
        has: categoryId
      }
    }
  })
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
    }
  })
  const categories = await prisma.category.findMany({
    where: {
      id: {
        in: Pallot.categoryIds,
      }
    }
  })
  return res.status(StatusCodes.ACCEPTED).json({ categories });
};