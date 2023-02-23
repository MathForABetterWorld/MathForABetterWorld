// Here the functions relating to account db operations will occur

import { StatusCodes } from "http-status-codes";

export const create = async (req, res) => {
  const { name, email } = req.body;
  const user = await prisma.user.create({ data: { name, email } });
  return res.status(StatusCodes.ACCEPTED).json({ user });
};
