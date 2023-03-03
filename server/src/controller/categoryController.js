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
 */
export const getCategoriesInWarehouse = async (req, res) => {
  if (validate(req, res)) {
    return res;
  }

  const [pallots, categories] = await Promise.all([prisma.pallot.findMany(), prisma.category.findMany()]);

  let categoryIds_set = new Set(); // no duplicates
  for (const pallot of pallots) {
    for (const categoryIds of pallot.categoryIds) {
      for (const categoryId of categoryIds) {
        categoryIds_set.add(categoryId);
      }
    }
  }
  let categoriesInWarehouse = new Set(); // no duplicates 
  for (const category of categories) {
    if (categoryIds.has(category.id)) { // only add the categories that are in the warehouse
      categoriesInWarehouse.add(category);
    }
  }
  categoriesInWarehouse = Array.from(categoriesInWarehouse); // finally, convert set back to array
  return res.status(StatusCodes.ACCEPTED).json({ categoriesInWarehouse });
};
