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
    if (validate(req, res)) {
        return res;
    }
    const trash = await prisma.trashItem.findMany({
        include: {  category: true, user: true},
    });
    return res.status(StatusCodes.ACCEPTED).json({ trash });
  };

  export const editTrash = async(req, res) => {
    if (validate(req, res)) {
        return res;
    }
    const id = req.id;
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

export const getExportsInDuration = async (req, res) => {
    const { duration } = req.params;
    const startDate = new Date();
    if (duration === "day") {
      startDate.setDate(startDate.getDate() - 1);
    } else if (duration === "week") {
      startDate.setDate(startDate.getDate() - 7);
    } else if (duration === "month") {
      startDate.setMonth(startDate.getMonth() - 1);
    } else {
      startDate.setFullYear(startDate.getFullYear() - 1);
    }
    startDate.setUTCHours(0);
    startDate.setUTCMinutes(0);
    startDate.setUTCSeconds(0);
    startDate.setUTCMilliseconds(0);
    const exportTotalInDuration = await prisma.trashItem.aggregate({
      _sum: {
        weight: true,
      },
      where: {
        trashDate: {
          gte: startDate,
        },
      },
    });
    return res.status(StatusCodes.ACCEPTED).json({ exportTotalInDuration });
  };