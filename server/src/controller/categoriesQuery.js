import validate from "../util/checkValidation.js";
import prisma from "../../prisma/client.js";
import { StatusCodes } from "http-status-codes";

/**
 * Is virtually the same as categoryController.js getCategory()
 * Task: query: list of categories in the warehouse #38
 */
export const getCategoriesInWarehouse = async (req, res) => {
  if (validate(req, res)) {
    return res;
  }

  const [pallots, categories] = await Promise.all([prisma.pallot.findMany(), prisma.category.findMany()]);
  
  let categoryIds = new Set(); // no duplicates
  for (const pallot of pallots) {
    for (const categoryIds of pallot.categoryIds) {
      for (const categoryId of categoryIds) {
        categoryIds.add(categoryId);
      }
    }
  }
  let categoriesInWarehouse = new Set(); // no duplicates // filter out only the categories that are in the warehouse
  for (const category of categories) {
    if (categoryIds.has(category.id)) {
      categoriesInWarehouse.push(category);
    }
  }
  return res.status(StatusCodes.ACCEPTED).json({ categoriesInWarehouse });
};
