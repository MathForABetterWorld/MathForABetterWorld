import prisma from "../../prisma/client.js";
import { StatusCodes } from "http-status-codes";
import { Role } from "@prisma/client";
import { hashPassword, verifyPassword } from "./password.js";

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
      userId: req.id,
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

export const isUserEmployeeAndNotAdmin = async (req, res, next) => {
  const { userId } = req.body;
  const employee = await prisma.employee.findUnique({
    where: {
      userId,
    },
  });
  if (employee === null || employee === undefined) {
    return res.status(StatusCodes.BAD_REQUEST).json({
      msg: "ERROR: user must be an employee before promotion to admin",
    });
  } else if (employee.role !== Role.Employee) {
    return res
      .status(StatusCodes.BAD_REQUEST)
      .json({ msg: "ERROR: user is already an admin!" });
  } else {
    next();
  }
};

export const isUserEmployee = async (req, res, next) => {
  const userId = req.id;
  const employee = await prisma.employee.findUnique({
    where: {
      userId,
    },
  });
  if (employee === null || employee === undefined) {
    return res.status(StatusCodes.BAD_REQUEST).json({
      msg: "ERROR: user must be an employee",
    });
  } else {
    next();
  }
};

export const loginMatches = async (req, res, next) => {
  const { password, userName } = req.body;
  const employee = await prisma.employee.findUnique({
    where: {
      userId: req.id,
    },
  });
  if (
    employee.userName !== userName ||
    !verifyPassword(password, employee.hashedPassword)
  ) {
    return res
      .status(StatusCodes.BAD_REQUEST)
      .json({ msg: "ERROR: old login does not match!" });
  } else {
    next();
  }
};
