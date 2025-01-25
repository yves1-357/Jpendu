import tkinter as tk

#Cree une premiere fenetre
fenetre = tk.Tk()

#Personnaliser cette fenetre
fenetre.title('Contacts')
fenetre.geometry('580x280')
fenetre['bg'] = '#E6E6E6'
fenetre.resizable(False, False)
#*******************************
#*** Ajout des texte #*******************
#********************************
tk.Label(fenetre, text="Nom").grid(row=0)
tk.Label(fenetre, text="Prenom").grid(row=3)
tk.Label(fenetre, text="Adresse").grid(row=5)
tk.Label(fenetre, text="Code Postal").grid(row=7)
tk.Label(fenetre, text="Ville").grid(row=9)

# Créer un Label pour afficher les " contacts "
contacts_label = tk.Label(fenetre, text="0 contacts")
contacts_label.place(x=250, y=185)

e1 = tk.Entry(fenetre,width=70)
e2 = tk.Entry(fenetre,width=70)
e3 = tk.Entry(fenetre,width=70)
e4 = tk.Entry(fenetre,width=70)
e5 = tk.Entry(fenetre,width=70)

e1.grid(row=0, column=1, padx=10, pady=37)
e2.grid(row=3, column=1, padx=10, pady=10)
e3.grid(row=5, column=1, padx=10, pady=10)
e4.grid(row=7, column=1, padx=10, pady=10)
e5.grid(row=9, column=1, padx=10, pady=10)

button = tk.Button(fenetre, text='Premier', bg='blue', fg='white')
button.place(x=3, y=210)

button = tk.Button(fenetre, text='Precedent', bg='blue', fg='white')
button.place(x=58, y=210)

button = tk.Button(fenetre, text='Nouveau', bg='blue', fg='white')
button.place(x=125, y=210)

button = tk.Button(fenetre, text='Sauver', bg='blue', fg='white')
button.place(x=185, y=210)

button = tk.Button(fenetre, text='Sauver&Nouveau', bg='blue', fg='white')
button.place(x=232, y=210)

button = tk.Button(fenetre, text='Supprimer', bg='blue', fg='white')
button.place(x=340, y=210)

button = tk.Button(fenetre, text='Suivant', bg='blue', fg='white')
button.place(x=410, y=210)

button = tk.Button(fenetre, text='Dernier', bg='blue', fg='white')
button.place(x=465, y=210)

button = tk.Button(fenetre, text='Quitter', bg='blue', fg='white')
button.place(x=520, y=210)



fenetre.mainloop()





export let cart = JSON.parse(localStorage.getItem('cart'));

if (!cart ){
cart = [{
productid: 'e43638ce-6aa0-4b85-b27f-e1d07eb678c6',
quantity: 2,
},{
    productid:'15b6fc6f-327a-4ec4-896f-486349e85a3d',
    quantity: 1
}];
}

function saveTostorage(){
    localStorage.setItem('cart',JSON.stringify(cart));
}

export function addToCart (productid){
    let matchingItem;

cart.forEach((cartItem) => {
if (productid === cartItem.productid){
    matchingItem = cartItem;

}

});

if (matchingItem){
matchingItem.quantity += 1;
} else {
cart.push({
productid: productid,
quantity: 1
});
}
}

export function removeFromCart(productid){
    const newCart = [];

cart.forEach((cartItem) => {
if (cartItem.productid !== productid){
    newCart.push(cartItem);
}
});
cart = newCart;
};
