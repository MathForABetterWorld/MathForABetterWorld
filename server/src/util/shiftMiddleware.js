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