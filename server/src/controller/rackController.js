import validate from "../util/checkValidation.js";
import prisma from "../../prisma/client.js";
import { StatusCodes } from "http-status-codes";

/**
 * Creates a food entry
 * @param {object} req - request for the course
 * @param {object} res - response for the request
 */
export const createRack = async (req, res) => {
  if (validate(req, res)) {
    return res;
  }
  const { id, location, description, weightLimit, foodEntry } = req.body;
  // const { id } = req.user;
  const rack = await prisma.rack.create({
    data: {
      id,
      location,
      description,
      weightLimit,
      foodEntry,
    },
  });
  return res.status(StatusCodes.CREATED).json({ rack });
};

/**
 * Gets list of food entrys
 * @param {object} req - request for the course
 * @param {object} res - response for the request
 */
export const getRack = async (req, res) => {
  const foodEntry = await prisma.foodEntry.findMany();
  return res.status(StatusCodes.ACCEPTED).json({ foodEntry });
};

/**
 * Deletes a food entry
 * @param {object} req - request for the course
 * @param {object} res - response for the request
 */
export const deleteRack = async (req, res) => {
  const id = parseInt(req.params.id, 10);
  const foodEntry = await prisma.foodEntry.delete({
    where: {
      id,
    },
  });
  return res.status(StatusCodes.ACCEPTED).json({ foodEntry });
};
