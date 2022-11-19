class AddNetworkDevicesTable < ActiveRecord::Migration[7.0]
  def change
    create_table :network_devices do |t|
      t.string :mac_address
      t.string :name

      t.timestamps
    end
  end
end
