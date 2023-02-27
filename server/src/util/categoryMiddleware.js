import prisma from "../../prisma/client.js";
import { StatusCodes } from "http-status-codes";


/**
 * checks if the category name being entered is unique
 * @param {object} req - request
 * @param {object} res - response
 * @param {object} next - call back function
 */

export const isUniqueName = async (req, res, next) => {
  const { name } = req.body;
  const query = await prisma.category.findFirst({
    where: {
      name,
    },
  });
  if (query !== null) {
    return res
      .status(StatusCodes.CONFLICT)
      .json({ msg: "ERROR: Category with this name already exists" });
  } else {
    next();
  }
};


/**
 * checks if the category being entered exists
 * @param {object} req - request
 * @param {object} res - response
 * @param {object} next - call back function
 */
export const isCategoryId = async (req, res, next) => {
    const id = parseInt(req.params.id, 10);
    const query = await prisma.category.findUnique({
      where: {
        id,
      },
    });
    if (query === null || query === undefined) {
      return res
        .status(StatusCodes.CONFLICT)
        .json({ msg: "ERROR: Category does not exist" });
    } else {
      next();
    }
  };