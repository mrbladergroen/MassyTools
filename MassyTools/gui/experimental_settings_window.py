from MassyTools.gui.tooltip import create_tooltip
import tkinter as tk


class ExperimentalSettingsWindow(object):
    def __init__(self, master):
        self.settings = master.settings
        self.building_blocks = master.building_blocks
        self.create_window()

    def close_settings_window(self):
        self.store_settings()
        self.root.destroy()

    def save_settings(self):
        self.store_settings()
        self.settings.save_to_disk()

    def store_settings(self):
        self.settings.charge_carrier = self.charge_carrier_var.get()
        mass_modifiers = []
        for mass_modifier in self.selected_modifier.get(0, tk.END):
            for building_block in self.building_blocks:
                if mass_modifier == self.building_blocks[building_block]['human_readable_name']:
                    mass_modifiers.append(building_block)
        self.settings.mass_modifiers = mass_modifiers

    def create_window(self):
        # This can be prettier
        def onselect1(evt):
            w = evt.widget
            index = int(w.curselection()[0])
            value = w.get(index)
            selected_modifier.insert(tk.END,value)
            available_modifier.delete(index)

        def onselect2(evt):
            w = evt.widget
            index = int(w.curselection()[0])
            value = w.get(index)
            selected_modifier.delete(index)
            available_modifier.insert(tk.END,value)

        root = tk.Toplevel()
        root.protocol( "WM_DELETE_WINDOW", self.close_settings_window)

        options = []
        charge_carrier_var = tk.StringVar()
        charge_carrier_var.set(self.settings.charge_carrier)

        experimental_label = tk.Label(
                root, text="Experimental parameters", font="bold")
        experimental_label.grid(row=1, columnspan=2, sticky=tk.W)

        charge_carrier_label = tk.Label(
                root, text="Charge Carrier")
        charge_carrier_label.grid(row=2, column=0, sticky=tk.W)
        for building_block in self.building_blocks:
            if self.building_blocks[building_block]['available_for_charge_carrier'] == 1:
                options.append(building_block)
        charge_carrier = tk.OptionMenu(root, charge_carrier_var, *options)
        charge_carrier.grid(row=2, column=1, sticky=tk.W)

        available_modifier_label = tk.Label(root, text='Available '+
                                            'Mass Modifiers')
        available_modifier_label.grid(row=3, column=0, sticky=tk.W)
        selected_modifier_label = tk.Label(root, text='Selected '+
                                           'Mass Modifiers')
        selected_modifier_label.grid(row=3, column=1, sticky=tk.W)

        available_modifier = tk.Listbox(root)
        available_modifier.grid(row=4, column=0, columnspan=2,
                                sticky=tk.W)
        available_modifier.bind('<<ListboxSelect>>', onselect1)
        selected_modifier = tk.Listbox(root)
        selected_modifier.grid(row=4, column=1, columnspan=2,
                               sticky=tk.W)
        selected_modifier.bind('<<ListboxSelect>>', onselect2)
        for building_block in self.building_blocks:
            if building_block in self.settings.mass_modifiers:
                selected_modifier.insert(tk.END, self.building_blocks[building_block]['human_readable_name'])
            elif self.building_blocks[building_block]['available_for_mass_modifiers'] == 1:
                available_modifier.insert(tk.END, self.building_blocks[building_block]['human_readable_name'])

        ok = tk.Button(root, text='Ok', command=self.close_settings_window)
        ok.grid(row=5, column=0, sticky=tk.W)
        save = tk.Button(root, text='Save', command=self.save_settings)
        save.grid(row=5, column=1, sticky=tk.E)

        # Self assignment
        self.root = root
        self.charge_carrier_var = charge_carrier_var
        self.selected_modifier = selected_modifier
        #self.minCharge = Spinbox(top, from_= 1, to = 3, width = 5)
        #self.minCharge.grid(row = 0, column = 2, sticky = W)
        #self.max = Label(top, text = "Max", width = 5)
        #self.max.grid(row = 0, column = 3, sticky = W)
        #self.maxCharge = Spinbox(top, from_ = 1, to=3, width=5)
        #self.maxCharge.grid(row = 0, column = 4, sticky = W)