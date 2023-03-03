import validate from "../util/checkValidation.js";
import prisma from "../../prisma/client.js";
import { StatusCodes } from "http-status-codes";

/**
 * Creates category
 * @param {object} req - request for the course
 * @param {object} res - response for the request
 */

export const createCategory = async (req, res) => {
  if (validate(req, res)) {
    return res;
  }
  const { name, description } = req.body;
  // const { id } = req.user;
  const category = await prisma.category.create({
    data: {
      name,
      description,
    },
  });
  return res.status(StatusCodes.CREATED).json({ category });
};

/**
 * READ a list of categories from the database
 * @param {object} req - request for the course
 * @param {object} res - response for the request
 */
export const getCategory = async (req, res) => {
  const category = await prisma.category.findMany();
  return res.status(StatusCodes.ACCEPTED).json({ category });
};

/**
 * UPDATE a category
 * @param {object} req - request for the course
 * @param {object} res - response for the request
 */
export const updateCategory = async (req, res) => {
  if (validate(req, res)) {
    return res;
  }
  const id = parseInt(req.params.id, 10);
  const { name, description } = req.body;
  const category = await prisma.category.update({
    where: {
      id,
    },
    data: {
      name,
      description,
    },
  });
  return res.status(StatusCodes.ACCEPTED).json({ category });
};

/**
 * DELETE a category
 * @param {object} req - request for the course
 * @param {object} res - response for the request
 */
export const deleteCategory = async (req, res) => {
  const id = parseInt(req.params.id, 10);
  const category = await prisma.category.delete({
    where: {
      id,
    },
  });
  return res.status(StatusCodes.ACCEPTED).json({ category });
};

/**
 * Is virtually the same as categoryController.js getCategory()
 * Task: query: list of categories in the warehouse #38
 *
 * This is effectively the same query you had before.
 * It just returns all categories, since a pallot will never be removed
 * from the DB as we need to track the total weight and history.
 * To check if something is in the warehouse, you need to check the field
 * inWarehouse and if it is true or false. This should be included in the
 * findMany query for pallots. Additionally, there is no need to query for
 * all the categories initially.
 * Instead, create a set of categoryIds (like you are currently doing),
 * and then query like so:
 * categories = await prisma.findMany({where : {id: { in: categoryIds}, }, });
 */
export const getCategoriesInWarehouse = async (req, res) => {
  if (validate(req, res)) {
    return res;
  }
  const pallots = await prisma.pallot.findMany({ 
    where: {
      inWarehouse: true, // only care about the categoryIds that are in the warehouse
    },
  });
  const categoryIds_set = new Set(pallots.flatMap(pallot => pallot.categoryIds)); // set, no duplicates, constant read access
  const categoriesInWarehouse = await prisma.category.findMany({
    where: {
      id: {
        in: categoryIds_set,
      },
    },
  });
  return res.status(StatusCodes.ACCEPTED).json({ categoriesInWarehouse });
};
