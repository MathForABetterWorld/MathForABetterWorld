import validate from "../util/checkValidation.js";
import prisma from "../../prisma/client.js";
import { StatusCodes } from "http-status-codes";

export const createTrash = async (req, res) => {
    if (validate(req, res)) {
      return res;
    }
    const {weight, categoryId, userId} = req.body;
    const trashItem = await prisma.trashItem.create({
        data: {
            weight,
            categoryId,
            userId,
        },
    });
    return res.status(StatusCodes.CREATED).json({ trashItem });
  };

  export const getTrash = async(req, res) => { 
    if (validate(req, res)) { //what does this do?
        return res;
    }
    const trash = await prisma.trashItem.findMany({
        include: {  weight: true, category: true}, //need to talk about what we want to include
    });
    return res.status(StatusCodes.ACCEPTED).json({ trash });
  };

  export const editTrash = async(req, res) => {
    if (validate(req, res)) {
        return res;
    }
    const {weight, trashDate, categoryId, userId} = req.body;
    const trashItem = await prisma.trashItem.update({
        where: {
            id,
        },
        data: {
            weight,
            trashDate,
            categoryId,
            userId,
        }
    });
    return res.status(StatusCodes.CREATED).json({ trashItem });
  };

  export const deleteTrash = async(req, res) => {
    if (validate(req, res)) {
        return res;
    }
    const id = parseInt(req.params.id, 10);
    const deletedTrash = await prisma.trashItem.delete({ where: { id } });
    return res.status(StatusCodes.ACCEPTED).json({ deleteTrash });
};
  

