import prisma from "../../prisma/client.js";
import { StatusCodes } from "http-status-codes";
import { Role } from "@prisma/client";

export const isUserId = async (req, res, next) => {
  const { userId } = req.body;
  const query = await prisma.user.findUnique({
    where: {
      id: userId,
    },
  });
  if (query === null) {
    return res
      .status(StatusCodes.CONFLICT)
      .json({ msg: "ERROR: user does not exist" });
  } else {
    next();
  }
};

export const isAdmin = async (req, res, next) => {
  const employee = await prisma.employee.findUnique({
    where: {
      id: req.id,
    },
  });
  if (employee.role === Role.Admin) {
    next();
  } else {
    return res
      .status(StatusCodes.FORBIDDEN)
      .json({ msg: "ERROR: only admins can promote users" });
  }
};
