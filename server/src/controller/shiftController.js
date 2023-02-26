import validate from "../util/checkValidation.js";
import prisma from "../../prisma/client.js";
import { StatusCodes } from "http-status-codes";

/**
 * CREATE a shift
 * @param {object} req - request for the course
 * @param {object} res - response for the request
 */
export const createShift = async (req, res) => {
  if (validate(req, res)) {
    return res;
  }
  const { id, user, userId, start, end, foodTaken} = req.body;
  // const { id } = req.user;
  const shift = await prisma.shift.create({
    data: {
      id,
      user,
      userId,
      start,
      end,
      foodTaken,
    },
  });
  return res.status(StatusCodes.CREATED).json({ shift });
};

/**
 * READ a list of shifts
 * @param {object} req - request for the course
 * @param {object} res - response for the request
 */
export const getShift = async (req, res) => {
  const shift = await prisma.shift.findMany();
  return res.status(StatusCodes.ACCEPTED).json({ shift });
};

/**
 * UPDATE a shift
 * @param {object} req - request for the course
 * @param {object} res - response for the request
 */
export const updateShift = async (req, res) => {
  if (validate(req, res)) {
    return res;
  }

  const { id, user, userId, start, end, foodTaken} = req.body;
  const shift = await prisma.shift.update({
    where: {
      id,
    },
    data: {
        user,
        userId,
        start,
        end,
        foodTaken,
    },
  });
  return res.status(StatusCodes.ACCEPTED).json({ shift });
};

/**
 * DELETE a shift
 * @param {object} req - request for the course
 * @param {object} res - response for the request
 */
export const deleteShift = async (req, res) => {
  const id = parseInt(req.params.id, 10);
  const shift = await prisma.shift.delete({
    where: {
      id,
    },
  });
  return res.status(StatusCodes.ACCEPTED).json({ shift });
};
