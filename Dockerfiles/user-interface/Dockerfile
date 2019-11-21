FROM node:12.2.0-alpine AS builder
WORKDIR /app
COPY . .
RUN yarn run build

FROM node:12.2.0-alpine
RUN yarn global add serve
WORKDIR /app
COPY --from=builder /app/build .
EXPOSE 8080
CMD ["serve", "-p", "8080", "-s", "."]
