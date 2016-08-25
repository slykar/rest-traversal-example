FROM python:3
COPY ./docker/entrypoint.sh /
ADD . /code
WORKDIR /code
# Install local packages in editable mode
RUN ls packages/spree.rest
RUN python setup.py develop
ENTRYPOINT ['/entrypoint.sh']
CMD ['pserve']