// interface.ts
// called `DataPort` because its actually passing an object as data.
export interface DataPort {
    port(data: object): void;
};