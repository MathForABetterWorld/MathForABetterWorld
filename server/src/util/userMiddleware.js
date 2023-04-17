import prisma from "../../prisma/client.js";
import { StatusCodes } from "http-status-codes";

export const isUniqueEmail = async (req, res, next) => {
  const { email } = req.body;
  const query = await prisma.user.findUnique({
    where: {
      email,
    },
  });
  if (query !== null && query !== undefined) {
    return res
      .status(StatusCodes.CONFLICT)
      .json({ msg: "ERROR: email already exists with a user" });
  } else {
    next();
  }
};

export const isUserId = async (req, res, next) => {
  const { id } = req.body;
  const query = await prisma.user.findUnique({
    where: {
      id,
    },
  });
  if (query === null || query === undefined) {
    return res
      .status(StatusCodes.CONFLICT)
      .json({ msg: "ERROR: user does not exist" });
  } else {
    next();
  }
};

export const isUniquePhoneNumber = async (req, res, next) => {
  const { phoneNumber } = req.body;
  if (phoneNumber != null) {
    const query = await prisma.user.findUnique({
      where: {
        phoneNumber,
      },
    });
    if (query !== null && query !== undefined) {
      return res
        .status(StatusCodes.CONFLICT)
        .json({ msg: "ERROR: phone number already exists with a user" });
    } else {
      next();
    }
  } else {
    next();
  }
};
