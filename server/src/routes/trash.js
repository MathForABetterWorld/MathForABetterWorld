import express from "express";
import { checkToken } from "../util/middleware.js";
import * as validator from "../util/trashMiddleware.js";
import * as controller from "../controller/trashController.js";
import * as express_validator from "express-validator";

const body = express_validator.body;
const param = express_validator.param;

const router = express.Router();
// Guide: https://www.prisma.io/docs/concepts/components/prisma-client/crud

router.post(
    "/",
    body("weight", "PLease include a positive weight exported!")
        .notEmpty()
        .isFloat({gt: 0.0}),
    body("categoryId", "Please include an integer category Id")
        .notEmpty()
        .isInt(),
    body("userId", "Please include an integer user ID")
        .notEmpty()
        .isInt(),

    validator.isCategoryId, 
    validator.isUserId,
    controller.createTrash

)




export default router;