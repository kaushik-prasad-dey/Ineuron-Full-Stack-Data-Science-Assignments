class ShoppingCart:
    def __init__(self):
        # Attribute
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        return f"Item '{item}' added to the shopping cart."

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            return f"Item '{item}' removed from the shopping cart."
        else:
            return f"Item '{item}' not found in the shopping cart."

    def view_cart(self):
        if not self.items:
            return "Shopping cart is empty."
        else:
            cart_content = "Items in the shopping cart:"
            for item in self.items:
                cart_content += f"\n- {item}"
            return cart_content

    def clear_cart(self):
        self.items = []
        return "Shopping cart cleared."

# Streamlit app
def shopping_cart_app():
    st.title("Shopping Cart App")

    # Create a session-specific ShoppingCart instance
    if 'cart' not in st.session_state:
        st.session_state.cart = ShoppingCart()

    option = st.selectbox("Choose an action:", ["Add Item", "Remove Item", "View Cart", "Clear Cart"])

    if option == "Add Item":
        item_to_add = st.text_input("Enter item to add:")
        if st.button("Add"):
            result = st.session_state.cart.add_item(item_to_add)
            st.success(result)

    elif option == "Remove Item":
        item_to_remove = st.text_input("Enter item to remove:")
        if st.button("Remove"):
            result = st.session_state.cart.remove_item(item_to_remove)
            st.success(result)

    elif option == "View Cart":
        result = st.session_state.cart.view_cart()
        st.success(result)

    elif option == "Clear Cart":
        if st.button("Clear Cart"):
            result = st.session_state.cart.clear_cart()
            st.success(result)
