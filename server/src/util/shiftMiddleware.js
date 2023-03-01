import prisma from "../../prisma/client.js";
import { StatusCodes } from "http-status-codes";

export const isShiftId = async (req, res, next) => {
  const id = parseInt(req.params.id, 10);
  const query = await prisma.shift.findUnique({
    where: {
      id,
    },
  });
  if (query === null || query === undefined) {
    return res
      .status(StatusCodes.CONFLICT)
      .json({ msg: "ERROR: shift does not exist" });
  } else {
    next();
  }
};

export const isShiftIdBody = async (req, res, next) => {
  const { id } = req.body;
  const query = await prisma.shift.findUnique({
    where: {
      id,
    },
  });
  if (query === null || query === undefined) {
    return res
      .status(StatusCodes.CONFLICT)
      .json({ msg: "ERROR: shift does not exist" });
  } else {
    next();
  }
};

export const isUserId = async (req, res, next) => {
  const { userId } = req.body;
  const query = await prisma.user.findUnique({
    where: {
      id: userId,
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

export const isValidTimeShift = async (req, res, next) => {
  const { start, end } = req.body;
  const query = await prisma.shift.findFirst({
    where: {
      start,
      end,
    },
  });
  if (query === null || query === undefined) {
    return res
      .status(StatusCodes.CONFLICT)
      .json({ msg: "ERROR: shift does not exist" });
  } else if (start > end) {
    return res
      .status(StatusCodes.CONFLICT)
      .json({ msg: "ERROR: shift start time cannot be greater than end time" });
  } else {
    next();
  }
};
