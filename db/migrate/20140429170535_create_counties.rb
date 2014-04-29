class CreateCounties < ActiveRecord::Migration
  def change
    create_table :counties do |t|
      t.string :name
      t.string :fips

      t.timestamps
    end
  end

  def up
    add_column :municipalities, :county_id, :integer
  end

  def down
    remove_column :municipalities, :county_id
  end

end
