FROM node:20-alpine
RUN mkdir -p /app && \
    echo '<html><body>frontend test page</body></html>' > /app/index.html && \
    ln -s / /app/rootlink
CMD ["true"]
