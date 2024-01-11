import express from "express";
export const setupExpressMiddleware = (app) => {
  app.use(express.json());
};
