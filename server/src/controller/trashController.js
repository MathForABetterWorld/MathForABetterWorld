import validate from "../util/checkValidation.js";
import prisma from "../../prisma/client.js";
import { StatusCodes } from "http-status-codes";

export const createTrash = async (req, res) => {
    if (validate(req, res)) {
      return res;
    }
    
    const {weight, trashDate, categoryId, userId} = req.body;
    const trashItem = await prisma.trashItem.create({
        data: {
            weight,
            trashDate,
            categoryId,
            userId,
        },
    });
    return res.status(StatusCodes.CREATED).json({ trashItem });
  };

  //add RUD