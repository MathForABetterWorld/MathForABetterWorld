import prisma from "../../prisma/client.js";
import { StatusCodes } from "http-status-codes";


export const isCategoryId = async (req, res, next) => {
    const { categoryId } = req.body;
    const query = await prisma.category.findUnique({
      where: {
        id: categoryId,
      },
    });
    if (query === null || query === undefined) {
      return res
        .status(StatusCodes.CONFLICT)
        .json({ msg: "ERROR: category does not exist" });
    } else {
      next();
    }
};


export const isUserId = async (req, res, next) => {
    const { userId  } = req.body;
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