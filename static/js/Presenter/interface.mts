// interface.ts
// called `FuncPort` because its executing a function inside the 'web view'
// from the 'screen presenter'.
export interface FuncPort {
    port(): void;
};