import validate from "../util/checkValidation.js";
import prisma from "../../prisma/client.js";
import { StatusCodes } from "http-status-codes";
import { hashPassword } from "../util/password.js";
import { Role } from "@prisma/client";
import { createToken } from "../util/token.js";

export const promoteUser = async (req, res) => {
  const { userId, username, password } = req.body;
  const employee = await prisma.employee.create({
    data: {
      userId,
      userName: username,
      hashedPassword: hashPassword(password),
      role: Role.Employee,
    },
  });
  delete employee["hashedPassword"];

  return res.status(StatusCodes.CREATED).json({ employee });
};

export const promoteToAdmin = async (req, res) => {
  const { userId } = req.body;
  const employee = await prisma.employee.update({
    where: {
      userId,
    },
    data: {
      role: Role.Admin,
    },
  });
  delete employee["hashedPassword"];

  return res.status(StatusCodes.ACCEPTED).json({ employee });
};

export const updateLogin = async (req, res, next) => {
  const { newPassword, newUsername } = req.body;
  let employee = await prisma.employee.update({
    where: {
      userId: req.id,
    },
    data: {
      userName: newUsername,
      hashedPassword: hashPassword(newPassword),
    },
    include: {
      user: true,
    },
  });
  //delete employee["hashedPassword"];
  //delete employee["token"];
  const {
    hashedPassword,
    createdAt,
    updatedAt,
    token: storedToken,
    ...userInfo
  } = employee;
  console.log({ ...userInfo });
  const token = createToken({ user: { ...userInfo } });
  employee = await prisma.employee.update({
    where: { userId: req.id },
    data: {
      token,
    },
  });
  delete employee["hashedPassword"];
  return res.status(StatusCodes.ACCEPTED).json({ employee });
};
