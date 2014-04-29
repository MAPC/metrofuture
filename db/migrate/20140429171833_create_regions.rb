class CreateRegions < ActiveRecord::Migration
  def change
    create_table :regions do |t|
      t.string :name
      t.string :rpa_name
      t.string :abbr

      t.timestamps
    end
  end

  def up
    add_column :municipalities, :region_id, :integer
  end

  def down
    remove_column :municipalities, :region_id
  end
end
