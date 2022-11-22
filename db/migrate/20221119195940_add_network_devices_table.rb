class AddNetworkDevicesTable < ActiveRecord::Migration[7.0]
  def change
    create_table :network_devices do |t|
      t.string :mac_address
      t.string :name
      t.datetime :detected_at, :datetime

      t.timestamps
    end

    add_index :network_devices, :mac_address, unique: true
  end
end
