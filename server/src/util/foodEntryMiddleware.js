import prisma from "../../prisma/client.js";
import { StatusCodes } from "http-status-codes";

/**
 * checks if the food being entered exists
 * @param {object} req - request
 * @param {object} res - response
 * @param {object} next - call back function
 */
export const isFoodEntryId = async (req, res, next) => {
  const id = parseInt(req.params.id, 10);
  const query = await prisma.distributor.findUnique({
    where: {
      id,
    },
  });
  if (query === NULL || query === undefined) {
    return res
      .status(StatusCodes.CONFLICT)
      .json({ msg: "ERROR: food id does not exist" });
  } else {
    next();
  }
};

/**
 * checks the expiration date is still good
 * @param {object} req - request
 * @param {object} res - response
 * @param {object} next - call back function
 */
export const isExpired = (req, res, next) => {
  const { expirationDate, inputDate } = req.body;
  const exp = new Date(expirationDate);
  const input = new Date(inputDate);
  input.setDate(input.getDate() + 4);
  if (exp.getTime() < input.getTime()) {
    res
      .status(StatusCodes.BAD_REQUEST)
      .json({
        msg: "ERROR: expiration date has passed or is less than 4 days away",
      });
  } else {
    next();
  }
};

// check if distributor id exists

// check if rack exists

// check if entry user id exists
