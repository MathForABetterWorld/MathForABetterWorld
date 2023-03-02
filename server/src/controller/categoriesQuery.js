import validate from "../util/checkValidation.js";
import prisma from "../../prisma/client.js";
import { StatusCodes } from "http-status-codes";

/**
 * Is virtually the same as categoryController.js getCategory() 
 * Task: query: list of categories in the warehouse #38
 */
export const getCategories = async (req, res) => {
  if (validate(req, res)) {
    return res;
  }
  const categories = await prisma.category.findMany();
  return res.status(StatusCodes.ACCEPTED).json({ categories });
};
