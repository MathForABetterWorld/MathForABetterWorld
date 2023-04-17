import prisma from "../../prisma/client.js";
import { StatusCodes } from "http-status-codes";

/**
 * checks if the location name being entered is unique
 * @param {object} req - request
 * @param {object} res - response
 * @param {object} next - call back function
 */

export const isUniqueName = async (req, res, next) => {
  const { name } = req.body;
  const query = await prisma.DonationLocation.findFirst({
    where: {
      name,
    },
  });
  if (query !== null) {
    return res
      .status(StatusCodes.CONFLICT)
      .json({ msg: "ERROR: Location with this name already exists" });
  } else {
    next();
  }
};

export const isUniqueNameNotId = async (req, res, next) => {
  const id = parseInt(req.params.id, 10);
  const { name } = req.body;
  const query = await prisma.DonationLocation.findFirst({
    where: {
      name,
    },
  });
  if (query !== null && query.id !== id) {
    return res
      .status(StatusCodes.CONFLICT)
      .json({ msg: "ERROR: Location with this name already exists" });
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
export const isLocationId = async (req, res, next) => {
  const id = parseInt(req.params.id, 10);
  const query = await prisma.DonationLocation.findUnique({
    where: {
      id,
    },
  });
  if (query === null || query === undefined) {
    return res
      .status(StatusCodes.CONFLICT)
      .json({ msg: "ERROR: Location does not exist" });
  } else {
    next();
  }
};

/**
 * checks if latitude is between -90 and 90
 * @param {object} req - request
 * @param {object} res - response
 * @param {object} next - call back function
 */
export const isValidLatitude = (req, res, next) => {
  const { latitude } = req.body;
  if (latitude < -90 || latitude > 90) {
    res.status(StatusCodes.BAD_REQUEST).json({
      msg: "ERROR: Latitude is not between -90 and 90",
    });
  } else {
    next();
  }
};

/**
 * checks if longitude is between -90 and 90
 * @param {object} req - request
 * @param {object} res - response
 * @param {object} next - call back function
 */
export const isValidLongitude = (req, res, next) => {
  const { latitude } = req.body;
  if (latitude < -180 || latitude > 180) {
    res.status(StatusCodes.BAD_REQUEST).json({
      msg: "ERROR: Longitude is not between -180 and 180",
    });
  } else {
    next();
  }
};
