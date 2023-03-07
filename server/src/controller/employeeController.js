import validate from "../util/checkValidation.js";
import prisma from "../../prisma/client.js";
import { StatusCodes } from "http-status-codes";
import { hashPassword } from "../util/password.js";
import { Role } from "@prisma/client";

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
  return res.status(StatusCodes.ACCEPTED).json({ employee });
};
