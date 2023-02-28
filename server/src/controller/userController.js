// Here the functions relating to account db operations will occur
import validate from "../util/checkValidation.js";
import { StatusCodes } from "http-status-codes";

export const create = async (req, res) => {
  if (validate(req, res)) {
    return res;
  }
  const { name, email } = req.body;
  const user = await prisma.user.create({ data: { name, email } });
  return res.status(StatusCodes.ACCEPTED).json({ user });
};

export const get = async (req, res) => {
  if (validate(req, res)) {
    return res;
  }
  const users = await prisma.user.findMany({});
  return res.status(StatusCodes.ACCEPTED).json({ users });
};

export const update = async (req, res) => {
  if (validate(req, res)) {
    return res;
  }
  const { email, id } = req.body;
  const user = await prisma.user.update({ where: { id }, data: { email } });
  return res.status(StatusCodes.ACCEPTED).json({ user });
};
