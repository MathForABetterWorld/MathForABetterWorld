import express from "express";
import { checkToken } from "../util/middleware.js";
import * as validator from "../util/categoryMiddleware.js";
import * as controller from "../controller/categoriesQuery.js";
import * as express_validator from "express-validator";

const body = express_validator.body;
const param = express_validator.param;
const router = express.Router(); // Guide: https://www.prisma.io/docs/concepts/components/prisma-client/crud

router.get("/", controller.getCategoriesInWarehouse);

export default router;
