// Si algun dia vuelco aqui, johan del futuro asegurate de entender esto
// puede ser muy interesante; aqui te dejo un link
// https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Proxy

const target = {
    message1: "hello",
    message2: "everyone",
    1: "numero 1"
}

const handler1 = {}

const handler2 = {
    get: function (target, prop, receiver) {
        return 'world'
    }
}

const proxy1 = new Proxy(target, handler1)

console.log(proxy1.message1)
console.log(proxy1.message2)

const proxy2 = new Proxy(target, handler2)

console.log(proxy2.message1)
console.log(proxy2.message2)
